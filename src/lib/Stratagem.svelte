<script lang="ts">
  import up from "../assets/arrow-up.png";
  import down from "../assets/arrow-down.png";
  import left from "../assets/arrow-left.png";
  import right from "../assets/arrow-right.png";
  import upActive from "../assets/arrow-up-active.png";
  import downActive from "../assets/arrow-down-active.png";
  import leftActive from "../assets/arrow-left-active.png";
  import rightActive from "../assets/arrow-right-active.png";
  import upError from "../assets/arrow-up-error.png";
  import downError from "../assets/arrow-down-error.png";
  import leftError from "../assets/arrow-left-error.png";
  import rightError from "../assets/arrow-right-error.png";
  import type { Direction } from "../types";
  import { createEventDispatcher, onMount } from "svelte";
  import { numberErrors, numberSuccess, streak } from "../stores";

  export let code: Direction[];
  export let icon: string;
  export let alt: string;
  export let name: string;

  const succeed = createEventDispatcher();

  let timeout: number | undefined;

  let currentInput: Direction[] = [];
  let error = false;

  const images = {
    up,
    down,
    left,
    right,
  };
  const imagesActive = {
    up: upActive,
    down: downActive,
    left: leftActive,
    right: rightActive,
  };
  const imagesError = {
    up: upError,
    down: downError,
    left: leftError,
    right: rightError,
  };

  function append(code: Direction[], current: Direction[], next: Direction): Direction[] {
    const invalid = current.find((dir, i) => code[i] !== dir) !== undefined;
    if (invalid) {
      return [];
    }
    if (code[current.length] !== next) {
      return [];
    }
    return [...current, next];
  }

  function getUrl(
    direction: Direction,
    currentInput: Direction[],
    index: number,
    isError: boolean
  ): string {
    if (isError) {
      return imagesError[direction];
    }

    if (index < currentInput.length) {
      return imagesActive[direction];
    }

    return images[direction];
  }

  function onDirection(
    e: CustomEvent<{
      direction: Direction;
    }>
  ) {
    const direction = e.detail.direction;
    const curInput = append(code, currentInput, direction);
    currentInput = [...curInput];
    console.log(code, curInput);
    if (curInput.length === 0) {
      numberErrors.update((x) => x + 1);
      streak.set(0);
      error = true;
      timeout = setTimeout(() => (error = false), 700);
    } else {
      if (timeout) clearTimeout(timeout);
      error = false;
    }

    if (curInput.length === code.length) {
      numberSuccess.update((x) => x + 1);
      streak.update((x) => x + 1);
      succeed("succeed", { name });
    }
  }

  onMount(() => {
    document.addEventListener("direction", onDirection);

    return () => {
      document.removeEventListener("direction", onDirection as any);
    };
  });
</script>

<div class="flex flex-col items-center justify-center gap-3">
  <h2 class="text-xl">{name}</h2>
  <div class="flex justify-center"><img src={icon} {alt} /></div>
  <div class="flex flex-row">
    {#each code as direction, i}
      <img src={getUrl(direction, currentInput, i, error)} alt={direction} />
    {/each}
  </div>
</div>

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
  import type { Direction } from "../types"

  export let code: Direction[];
  export let icon: string;
  export let alt: string;
  export let name: string;
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

  const keymaps: Record<string, Direction> = {
    KeyA: "left",
    KeyW: "up",
    KeyS: "down",
    KeyD: "right",
    KeyH: "left",
    KeyK: "up",
    KeyJ: "down",
    KeyL: "right",
    ArrowLeft: "left",
    ArrowUp: "up",
    ArrowDown: "down",
    ArrowRight: "right",
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

  function handleKeydown(
    event: KeyboardEvent & {
      currentTarget: EventTarget & Window;
    }
  ) {
    const direction = keymaps[event.code];
    if (direction === undefined) {
      return;
    }
    currentInput = append(code, currentInput, direction);
    if (currentInput.length === 0) {
      error = true;
      timeout = setTimeout(() => (error = false), 700);
    } else {
      if (timeout) clearTimeout(timeout);
      error = false;
    }

    if (currentInput.length === code.length){
      setTimeout(() => currentInput = [], 1000);
    }
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
</script>

<svelte:window on:keydown={handleKeydown} />

<div>
  <h2 class="text-xl">{name}</h2>
  <img src={icon} {alt}>
  <div class="flex flex-row">
    {#each code as direction, i}
      <img src={getUrl(direction, currentInput, i, error)} alt={direction} />
    {/each}
  </div>
</div>

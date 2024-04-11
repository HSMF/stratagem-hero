<script lang="ts">
  import Stratagem from "./lib/Stratagem.svelte";
  import type { Stratagem as StratagemT } from "./types";
  import stratagems from "./stratagems.json";
  import { contains } from "./utils";
  import logo from "/logo.png";
  import KeyListener from "./lib/KeyListener.svelte";
  import MobileControls from "./lib/MobileControls.svelte";
  import { keysPressed, numberErrors } from "./stores";
  import Streak from "./lib/Streak.svelte";

  const previewLimit = 5;

  function cast<T>(x: unknown): T {
    return x as T;
  }

  function shuffle<T>(myArr: T[]): T[] {
    const array = [...myArr];
    let currentIndex = array.length;

    // While there remain elements to shuffle...
    while (currentIndex != 0) {
      // Pick a remaining element...
      let randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;

      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
    }
    return array;
  }

  let nextStratagems = shuffle(stratagems);
  let head: StratagemT;
  let next: StratagemT[];
  let unique = {};
  $: {
    [head, ...next] = nextStratagems;
  }
  let score = 0;

  function advance() {
    let [_, ...newThing] = nextStratagems;
    score++;
    if (newThing.length <= 10) {
      console.log("shuffling");
      const seen = newThing.slice(1, previewLimit + 1);
      const fresh = shuffle(stratagems.filter((x) => !contains(seen, x)));

      newThing = seen.concat(fresh);
    }
    unique = {};
    nextStratagems = newThing;
  }

  $: accuracy = Math.round((($keysPressed - $numberErrors) / $keysPressed) * 1000) / 10;
  function accuracyColor(accuracy: number): string {
    if (Number.isNaN(accuracy)) {
      return "";
    }
    if (accuracy >= 95) {
      return "text-mauve";
    }
    if (accuracy >= 90) {
      return "text-blue";
    }
    if (accuracy >= 85) {
      return "text-green";
    }
    if (accuracy >= 80) {
      return "text-yellow";
    }
    if (accuracy >= 70) {
      return "text-peach";
    }
    if (accuracy >= 60) {
      return "text-peach";
    }
    return "text-red";
  }

  document.addEventListener('direction', e => {
    console.log(e)
    keysPressed.update((x) => x + 1);
  })
</script>

<svelte:body class="frappe bg-base" />

<main class="text-text flex h-screen justify-center">
  <KeyListener />
  <div class="flex flex-col items-center gap-2 p-2">
    <img src={logo} alt="HELLDIVERS" />
    <div
      class="bg-mantle border-subtext1 flex flex-col items-center gap-5 rounded-lg border px-3 py-6 shadow-lg"
    >
      <div>
      <h2 class="text-xl">
        Score {score} / {$keysPressed} /
        <span class="text-red">{$numberErrors}</span>
      </h2>
      <h2 class={"text-xl font-bold drop-shadow-md " + accuracyColor(accuracy)}>
        Accuracy {accuracy}
      </h2>

      </div>
      <div class="flex gap-2">
        {#each nextStratagems.slice(1, 1 + previewLimit) as preview}
          <img src={preview.path} alt={preview.alt} />
        {/each}
      </div>
      {#key unique}
        <Stratagem
          on:succeed={() => advance()}
          icon={head.path}
          code={cast(head.code)}
          name={head.name}
          alt={head.alt}
        />
      {/key}

      <Streak />

      <span>
        Official S.E.A.F. approved stratagem training terminal <span style="font-size: 6pt;">
          not really
        </span>
      </span>
    </div>

    <MobileControls />
  </div>
</main>

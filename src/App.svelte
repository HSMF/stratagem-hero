<script lang="ts">
  import Stratagem from "./lib/Stratagem.svelte";
  import type { Stratagem as StratagemT } from "./types";
  import stratagems from "./stratagems.json";
  import { contains } from "./utils";
  import logo from "/logo.png";

  const previewLimit = 10;

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
    nextStratagems = nextStratagems.slice(1);
    score++;
    if (nextStratagems.length <= 10) {
      const seen = next.slice(0, previewLimit);
      const fresh = shuffle(stratagems.filter((x) => !contains(seen, x)));

      nextStratagems = seen.concat(fresh);
    }
    unique = {};
  }
</script>

<main class="frappe bg-base text-text flex h-screen justify-center">
  <div class="flex flex-col items-center p-2">
    <img src={logo} alt="" />
    <div
      class="bg-mantle border-subtext1 flex flex-col items-center gap-5 rounded-lg border px-3 py-6 shadow-lg"
    >
      <span class="text-xl">Score {score}</span>
      <div class="flex gap-2">
        {#each next.slice(0, previewLimit) as preview}
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
    </div>
  </div>
</main>

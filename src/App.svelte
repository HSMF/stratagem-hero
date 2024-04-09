<script lang="ts">
  import Stratagem from "./lib/Stratagem.svelte";
  import stratagems from './stratagems.json';
  function cast<T>(x: unknown): T{
    return x as T;
  }
</script>

<main>

  {#each stratagems as stratagem}
    <Stratagem icon={stratagem.path} code={cast(stratagem.code)} name={stratagem.name} alt={stratagem.alt}/>
  {/each}

</main>

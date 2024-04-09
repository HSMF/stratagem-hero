<script lang="ts">
  import up from "../assets/arrow-up.png";
  import down from "../assets/arrow-down.png";
  import left from "../assets/arrow-left.png";
  import right from "../assets/arrow-right.png";
  import type { Direction } from "../types";

  function onClick(direction: Direction) {
    return () => {
      document.dispatchEvent(new CustomEvent("direction", { detail: { direction } }));
    };
  }
</script>

<div class="flex flex-col items-center justify-center">
  <button class="" on:click={onClick("up")}><img class="w-10" src={up} alt="up" /></button>
  <div>
    <button class="" on:click={onClick("left")}><img class="w-10" src={left} alt="left" /></button>
    <button class="" on:click={onClick("down")}><img class="w-10" src={down} alt="down" /></button>
    <button class="" on:click={onClick("right")}>
      <img class="w-10" src={right} alt="right" />
    </button>
  </div>
</div>

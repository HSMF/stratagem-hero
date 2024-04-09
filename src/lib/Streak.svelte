<script lang="ts">
  import { streak } from "../stores";

  const stages = [
    "skull.png",
    "skull-1.png",
    "skull-2.png",
    "skull-3.png",
    "skull-4.png",
    "skull-5.png",
    "skull-6.png",
    "skull-7.png",
  ];

  let stage = 0;
  $: src = stages[stage];

  $: {
    for (let i = 0; i < 8; i++) {
      if ($streak < 5 + 5 * i) {
        stage = i;
        break;
      }
    }
  }
</script>

<div class="flex gap-2 font-bold" style="color: #FEE800;" class:hidden={$streak < 3}>
  <img class="h-6" {src} alt="skull" />
  x {$streak}
</div>

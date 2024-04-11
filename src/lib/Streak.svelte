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
  $: animation = ((stage) => {
    if (stage < 2) return "";
    if (stage < 3) return "shake-1 vertical-shaking";
    if (stage < 5) return "shake-2 vertical-shaking";
    return "shake-3 vertical-shaking";
  })(stage);

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
  <img class={"h-6 " + animation} {src} alt="skull" />
  x {$streak}
</div>

<style>
  div {
    animation: horizontal-shaking 100ms linear infinite;
  }

  .shake-none {
    animation: none;
  }

  .shake-1 {
    animation: horizontal-shaking-1 100ms linear infinite;
  }

  .shake-2 {
    animation: horizontal-shaking-2 100ms linear infinite;
  }

  .shake-3 {
    animation: horizontal-shaking-3 100ms linear infinite;
  }

  .shake-y {
    animation: vertical-shaking-2 125ms linear infinite;
  }

  @keyframes vertical-shaking-2 {
    0% {
      transform: translateY(0);
    }
    25% {
      transform: translateY(2px);
    }
    50% {
      transform: translateY(-2px);
    }
    75% {
      transform: translateY(2px);
    }
    100% {
      transform: translateY(0);
    }
  }

  @keyframes horizontal-shaking-3 {
    0% {
      transform: translateX(0);
    }
    25% {
      transform: translateX(3px);
    }
    50% {
      transform: translateX(-3px);
    }
    75% {
      transform: translateX(3px);
    }
    100% {
      transform: translateX(0);
    }
  }

  @keyframes horizontal-shaking-1 {
    0% {
      transform: translateX(0);
    }
    25% {
      transform: translateX(1px);
    }
    50% {
      transform: translateX(-1px);
    }
    75% {
      transform: translateX(1px);
    }
    100% {
      transform: translateX(0);
    }
  }

  @keyframes horizontal-shaking-2 {
    0% {
      transform: translateX(0);
    }
    25% {
      transform: translateX(2px);
    }
    50% {
      transform: translateX(-2px);
    }
    75% {
      transform: translateX(2px);
    }
    100% {
      transform: translateX(0);
    }
  }
</style>

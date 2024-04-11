<script lang="ts">
  import { keysPressed } from "../stores";
  import type { Direction } from "../types";

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

  function handleKeydown(
    event: KeyboardEvent & {
      currentTarget: EventTarget & Window;
    }
  ) {
    const direction = keymaps[event.code];
    if (direction === undefined) {
      return;
    }
    document.dispatchEvent(new CustomEvent("direction", { detail: { direction } }));
  }
</script>

<svelte:window on:keydown={handleKeydown} />

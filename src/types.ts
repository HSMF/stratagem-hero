import stratagems from "./stratagems.json";
export type Direction = "up" | "down" | "left" | "right";
export type Stratagem = (typeof stratagems)[number];

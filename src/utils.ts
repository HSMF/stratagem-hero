export function contains<T>(arr: T[], el: T): boolean {
  return arr.find((x) => el === x) !== undefined;
}

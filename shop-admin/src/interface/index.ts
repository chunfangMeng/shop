export type PageResponse<T> = {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export type DefaultTableOptions = {
  options: [number, string][];
  name: string;
  classify: string;
  placeholder?: string;
}
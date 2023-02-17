

export namespace ProductTagModule {
  export type TagInfo = {
    id?: number;
    back_color: string;
    content: string;
    create_at: string;
    goods_bind_count: number;
    index: number;
    last_update: string;
    name: string;
    text_color: string;
  }

  export type TagFilter = {
    createRange?: []
  }
}
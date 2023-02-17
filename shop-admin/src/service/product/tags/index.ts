import ApiHttp from "@/api";
import { PageResponse } from "@/interface";
import { ProductTagModule } from "@/interface/product/tags";

class ProductTagService extends ApiHttp {
  getProductTags = (params?: ProductTagModule.TagFilter) => this.get<PageResponse<ProductTagModule.TagInfo>>('/api/v1/product/goods/tags/', params)
  UpdateGoodsTag = (values: ProductTagModule.TagInfo) => this.put(`/api/v1/product/goods/tags/${values.id}/`, values)
  createGoodsTag = (values: ProductTagModule.TagInfo) => this.post('/api/v1/product/goods/tags/', values)
}

const productTagsService = new ProductTagService()

export default productTagsService;
import ApiHttp from "@/api";
import { PageResponse } from "@/interface";
import { ProductTagModule } from "@/interface/product/tags";

class ProductTagService extends ApiHttp {
  getProductTags = () => this.get<PageResponse<ProductTagModule.TagInfo>>('/api/v1/product/goods/tags/')
  UpdateGoodsTag = (values: ProductTagModule.TagInfo) => this.put(`/api/v1/product/goods/tags/${values.id}/`, values)
}

const productTagsService = new ProductTagService()

export default productTagsService;
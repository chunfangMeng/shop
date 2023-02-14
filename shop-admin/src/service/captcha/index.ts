import ApiHttp from "@/api";
import { CaptchaResponse } from "@/interface/auth";

class CaptchaService extends ApiHttp {
  getCaptchaImage = () => this.get<CaptchaResponse>('/api/v1/web/captcha/')
}

const captchaService = new CaptchaService();

export default captchaService;
import { LoginForm, LoginResponse } from "../../interface/auth";
import { DefaultTableOptions, PageResponse } from "@/interface";
import ApiHttp from "@/api";
import { ManagerUser } from "@/interface/staff";

class MemberService extends ApiHttp {
  loginAuth = (values: LoginForm) => this.post<LoginResponse>('/api/v1/manager/login/', values)
  logoutAuth = () => this.post('/api/v1/manager/logout/')
  getManagerUserInfo = () => this.get<ManagerUser.UserInfo>('/api/v1/manager/info/')
  getManagerStaffList = () => this.get<PageResponse<ManagerUser.UserInfo>>('/api/v1/manager/');
  getStaffListOptions = () => this.get<DefaultTableOptions[]>('/api/v1/manager/options/')
  createStaff = (values: ManagerUser.UserInfo) => this.post('/api/v1/manager/register/', values)
  updateStaff = (values: ManagerUser.UserInfo) => this.put(`/api/v1/manager/${values.id}/`, values)
}

const memberService = new MemberService();

export default memberService;
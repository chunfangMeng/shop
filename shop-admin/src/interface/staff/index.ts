import { UserObject } from "../auth";

export namespace ManagerUser {
  export type UserInfo = {
    gender: number;
    id?: number;
    manage_number?: string;
    nickname: string;
    phone: string | null;
    profile_photo?: string | null;
    user: UserObject;
  }

  export type StaffListFilter = {
    dateRange: undefined
    gender?: string;
    keyword?: string;
  }
}
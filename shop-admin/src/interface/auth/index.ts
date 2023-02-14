
export type CaptchaResponse = {
  base64_image: string;
  hash_key: string;
}

export type LoginForm = {
  username: string;
  password: string;
  hash_key: string;
  captcha_code: string;
}

export type LoginResponse = {
  token: string;
}

export type UserObject = {
  email: string;
  first_name: string;
  is_active?: boolean;
  is_staff?: boolean;
  last_name: string;
  username: string;
}
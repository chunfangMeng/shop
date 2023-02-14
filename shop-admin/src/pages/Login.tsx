import captchaService from "@/service/captcha";
import { Button, Image, Form, Input, Spin, message } from "antd";
import { useNavigate } from "react-router-dom";
import { LoginForm } from "../interface/auth";
import useSWR from "swr";
import useSWRMutation from 'swr/mutation';
import memberService from "@/service/auth";


export default function Login() {
  const [ loginForm ] = Form.useForm()
  const navigate = useNavigate()
  const captcha = useSWR('captcha', captchaService.getCaptchaImage, {
    revalidateIfStale: false,
    revalidateOnFocus: false,
    onSuccess: res => {
      if (res.code === 200) {
        loginForm.setFieldsValue({hash_key: res.data.hash_key})
      }
    }
  })

  const { trigger } = useSWRMutation('/login', (key, options) => {
    return memberService.loginAuth(options.arg)
  }, {
    onSuccess: res => {
      if (res.code === 200) {
        message.success(res.message)
        localStorage.setItem('http_token', res.data.token)
        navigate('/')
      }
    }
  })

  const onLogin = (values: LoginForm) => {
    trigger(values)
  }
  return (
    <div className="container mx-auto px-4 w-4/12 m-9 border-2 border-indigo-60 p-10 pl-16 pr-16 shadow-md">
      <Form
        form={loginForm}
        onFinish={onLogin}
        initialValues={{ remember: true }}
        autoComplete="off"
        labelCol={{span: 5}}>
        <Form.Item
          label="用户名"
          name="username"
          rules={[{ required: true, message: '请输入用户名' }]}
        >
            <Input placeholder="用户名"/>
        </Form.Item>

        <Form.Item
            label="密码"
            name="password"
            rules={[{ required: true, message: '请输入密码' }]}
        >
            <Input.Password className="h-8" placeholder="密码"/>
        </Form.Item>

        <Form.Item
            hidden
            name="hash_key">
            <Input />
        </Form.Item>

        <Form.Item
            label="验证码"
            required>
            <div className="flex">
              <Form.Item
                name='captcha_code'
                noStyle
                rules={[
                    {required: true, message: '请输入验证码'}
                ]}>
                <Input maxLength={4} className="h-8" placeholder="验证码"/>
              </Form.Item>
              <div className="ml-4">
                {
                  captcha.isLoading ? 
                  <Spin tip="Loading" delay={500}>
                    <div className="content" />
                  </Spin> :
                  <Image
                    src={`data:image/jpg;base64,${captcha.data?.data.base64_image}`}
                    preview={false}
                    height={32}
                    width={80} />
                }
              </div>
            </div>
          </Form.Item>

          <Form.Item wrapperCol={{ offset: 5, span: 19 }}>
            <Button type="primary" htmlType="submit">
                Login
            </Button>
          </Form.Item>
      </Form>
    </div>
  )
}

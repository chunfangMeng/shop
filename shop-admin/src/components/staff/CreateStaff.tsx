import { Button, Drawer, Form, Input, Radio } from "antd";
import useSWRMutation from 'swr/mutation';
import React, { useEffect } from "react";
import memberService from "@/service/auth";
import { ManagerUser } from "@/interface/staff";

type CreateStaffProps = {
  visible: boolean;
  editRecord?: ManagerUser.UserInfo;
  onClose(): void;
}
const CreateStaff: React.FC<CreateStaffProps> = (props) => {
  const [ createForm ] = Form.useForm()
  const genderOptions = [{
    label: '未知',
    value: 0
  }, {
    label: '男',
    value: 1
  }, {
    label: '女',
    value: 2
  }, {
    label: '保密',
    value: 3
  }]
  const createStaff = useSWRMutation('/manager/register/', (key, options) => {
    return memberService.createStaff(options.arg)
  })
  const updateStaff = useSWRMutation('manager/update/', (key, options) => {
    return memberService.updateStaff(options.arg)
  })
  const onRegister = (values: ManagerUser.UserInfo) => {
    if (typeof props.editRecord !== "undefined") {
      updateStaff.trigger(values)
      return false
    }
    createStaff.trigger(values)
  }
  useEffect(() => {
    if (props.visible) createForm.resetFields()
  }, [props.visible])
  return (
    <Drawer 
      title={props.editRecord ? "编辑员工账号" : "创建员工账号"}
      placement="right" 
      onClose={props.onClose} 
      open={props.visible}>
      <Form
        form={createForm}
        onFinish={onRegister}
        initialValues={props.editRecord}>
        {
          typeof props.editRecord !== "undefined" &&
          <Form.Item
            hidden
            name="id">
            <Input />
          </Form.Item>
        }
        <Form.Item
          label="用户名"
          name={['user', 'username']}
          rules={[
            {required: true, message: '请输入用户名'}
          ]}>
          <Input showCount maxLength={150} readOnly={typeof props.editRecord !== "undefined"}/>
        </Form.Item>
        {
          typeof props.editRecord === "undefined" &&
          <Form.Item
            label="密码"
            name={['user', 'password']}
            rules={[
              {required: true, message: '请输入密码'}
            ]}>
            <Input.Password />
          </Form.Item>
        }
        <Form.Item
          label="邮箱"
          name={['user', 'email']}
          rules={[
            {required: true, message: '请输入邮箱'}
          ]}>
          <Input />
        </Form.Item>
        <Form.Item
          label="名称"
          name={'nickname'}
          rules={[
            {required: true, message: '请输入名称'}
          ]}>
          <Input />
        </Form.Item>
        <Form.Item
          label="性别"
          name="gender"
          rules={[
            {required: true, message: '请选择性别'}
          ]}>
          <Radio.Group options={genderOptions}/>
        </Form.Item>
        <Form.Item
          label="联系电话"
          name={'phone'}>
          <Input />
        </Form.Item>
        {/* <Form.Item
          label="头像"
          name="profile_photo">
          <SectionUpload />
        </Form.Item> */}
        <Form.Item>
          <Button htmlType="submit" type="primary">提交</Button>
        </Form.Item>
      </Form>
    </Drawer>
  )
}

export default React.memo(CreateStaff);
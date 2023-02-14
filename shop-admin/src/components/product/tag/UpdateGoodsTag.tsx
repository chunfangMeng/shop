import ColorPicker from '@/components/Color/ColorPicker';
import { ProductTagModule } from '@/interface/product/tags';
import { Button, Drawer, Form, Input, message, Tag } from 'antd';
import useSWRMutation from 'swr/mutation';
import React, { useEffect, useState } from 'react';
import productTagsService from '@/service/product/tags';

type UpdateGoodsTagProps = {
  editTag?: ProductTagModule.TagInfo;
  open: boolean;
  onClose(): void;
  onFinish(): void;
}
export default function UpdateGoodsTag(props: UpdateGoodsTagProps) {
  const [ tagForm ] = Form.useForm()
  const [ previewTextColor, setPreviewTextColor ] = useState<string>()
  const [ previewBgColor, setPreviewBgColor ] = useState<string>()
  const updateTag = useSWRMutation('/update/tag/', (key, options) => {
    return productTagsService.UpdateGoodsTag(options.arg)
  }, {
    onSuccess: res => {
      if (res.code === 200) {
        message.success(res.message)
        props.onFinish()
      }
    }
  })
  const onValuesChange = (changedValues: ProductTagModule.TagInfo, values: ProductTagModule.TagInfo) => {
    if (Object.keys(changedValues).includes('text_color')) {
      setPreviewTextColor(changedValues['text_color'])
    }
    if (Object.keys(changedValues).includes('back_color')) {
      setPreviewBgColor(changedValues['back_color'])
    }
  }
  const onTagFinish = (values: ProductTagModule.TagInfo) => {
    updateTag.trigger(values)
  }
  useEffect(() => {
    if (props.open && props.editTag) {
      setPreviewTextColor(props.editTag.text_color)
      setPreviewBgColor(props.editTag.back_color)
    }
  }, [props.open])
  return (
    <Drawer
      {...props}
      title={props.editTag ? "编辑标签" : "创建标签"}
      placement="right"
      extra={
        <Button type="primary" onClick={() => tagForm.submit()}>提交</Button>
      }>
      <Form
        form={tagForm}
        initialValues={props.editTag}
        onValuesChange={onValuesChange}
        onFinish={onTagFinish}>
        {
          props.editTag &&
          <Form.Item
            hidden
            name="id">
            <Input />
          </Form.Item>
        }
        <Form.Item
          label="标签名称"
          name="name"
          rules={[
            {required: true, message: '请输入标签名称'}
          ]}>
          <Input showCount maxLength={32}/>
        </Form.Item>
        <Form.Item
          label="标签描述"
          name="content">
          <Input.TextArea showCount maxLength={64} />
        </Form.Item>
        <Form.Item
          label="样式预览">
          <Tag style={{color: previewTextColor ?? '', borderColor: previewBgColor ?? ''}}>预览标签</Tag>
        </Form.Item>
        <Form.Item
          label="内容颜色"
          name="text_color">
          <ColorPicker />
        </Form.Item>
        <Form.Item
          label="背景颜色"
          name="back_color">
          <ColorPicker />
        </Form.Item>
      </Form>
    </Drawer>
  )
}
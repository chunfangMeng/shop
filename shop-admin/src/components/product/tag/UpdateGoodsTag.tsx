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
  const createTag = useSWRMutation('/create/tag/', (key, options) => {
    return productTagsService.createGoodsTag(options.arg)
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
    if (props.editTag) {
      updateTag.trigger(values)
      return false
    }
    createTag.trigger(values)
  }
  useEffect(() => {
    if (props.open && props.editTag) {
      setPreviewTextColor(props.editTag.text_color)
      setPreviewBgColor(props.editTag.back_color)
    }
    if (props.open && !props.editTag) {
      setPreviewTextColor(undefined)
      setPreviewBgColor(undefined)
    }
    tagForm.resetFields()
  }, [props.open])
  return (
    <Drawer
      {...props}
      title={props.editTag ? "????????????" : "????????????"}
      placement="right"
      extra={
        <Button type="primary" onClick={() => tagForm.submit()}>??????</Button>
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
          label="????????????"
          name="name"
          rules={[
            {required: true, message: '?????????????????????'}
          ]}>
          <Input showCount maxLength={32}/>
        </Form.Item>
        <Form.Item
          label="????????????"
          name="content">
          <Input.TextArea showCount maxLength={64} />
        </Form.Item>
        <Form.Item
          label="????????????">
          <Tag style={{color: previewTextColor ?? '', borderColor: previewBgColor ?? ''}}>????????????</Tag>
        </Form.Item>
        <Form.Item
          label="????????????"
          name="text_color">
          <ColorPicker />
        </Form.Item>
        <Form.Item
          label="????????????"
          name="back_color">
          <ColorPicker />
        </Form.Item>
      </Form>
    </Drawer>
  )
}
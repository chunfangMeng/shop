import DatePicker from '@/components/datetime/DateRange';
import UpdateGoodsTag from '@/components/product/tag/UpdateGoodsTag';
import { ProductTagModule } from '@/interface/product/tags';
import productTagsService from '@/service/product/tags';
import { Button, Card, Form, Input, Table, TableProps, Tag } from 'antd';
import React, { useState } from 'react';
import useSWR from "swr";


export default function TagsList() {
  const tagsList = useSWR('tagList', productTagsService.getProductTags)
  const [ editTag, setEditTag ] = useState<ProductTagModule.TagInfo>()
  const [ updateTagVisible, setUpdateTagVisible ] = useState(false)
  const onShowUpdate = (record?: ProductTagModule.TagInfo) => {
    setEditTag(record);
    setUpdateTagVisible(true);
  }
  const onUpdateFinish = () => {
    setUpdateTagVisible(false)
  }
  const tagTableProps: TableProps<ProductTagModule.TagInfo> = {
    columns: [{
      title: '标签名称',
      dataIndex: 'name',
      render: (text, record) => (
        <Tag style={{color: record.text_color ?? '', borderColor: record.back_color ?? ''}}>{text}</Tag>
      )
    }, {
      title: '标签描述',
      dataIndex: 'content'
    }, {
      title: '商品数量',
      dataIndex: 'goods_bind_count',
      render: (count, record) => (
        <span className='text-[#409EFF]'>{count}</span>
      )
    }, {
      title: '操作',
      dataIndex: 'action',
      render: (text, record) => (
        <Button ghost type="primary" onClick={() => onShowUpdate(record)}>编辑</Button>
      )
    }],
    rowKey: 'name',
    dataSource: tagsList.data?.data.results,
    loading: tagsList.isLoading
  }
  return (
    <>
      <Card className='mb-4'>
        <div className="flex justify-between">
          <Form
            className='m-0!'
            layout="inline">
            <Form.Item>
              <Input placeholder="输入关键字搜索"/>
            </Form.Item>
            <Form.Item>
              <Button ghost htmlType="submit" type="primary">筛选</Button>
            </Form.Item>
            <Form.Item>
              <Button>重置</Button>
            </Form.Item>
          </Form>
          <Button type="primary" onClick={() => onShowUpdate()}>创建</Button>
        </div>
      </Card>
      <Card>
        <Table {...tagTableProps}/>
        <UpdateGoodsTag 
          editTag={editTag}
          open={updateTagVisible}
          onClose={() => setUpdateTagVisible(false)}
          onFinish={onUpdateFinish}/>
      </Card>
    </>
  )
}
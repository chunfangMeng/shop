import memberService from "@/service/auth";
import { ColumnHeightOutlined, EditOutlined, FilterOutlined, PlusOutlined, RedoOutlined, RightOutlined, UndoOutlined } from "@ant-design/icons";
import { Button, Card, Form, Input, Select, Space, Table, TableProps, Tooltip } from "antd";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import DatePicker from "../../components/datetime/DateRange";
import useSWR from "swr";
import CreateStaff from "@/components/staff/CreateStaff";
import { ManagerUser } from "@/interface/staff";

export default function StaffList() {
  const [ createVisible, setCreateVisible ] = useState(false)
  const staffList = useSWR('captcha', memberService.getManagerStaffList)
  const staffOptions = useSWR('staffOptions', memberService.getStaffListOptions)
  const [ editRecord, setEditRecord ] = useState<ManagerUser.UserInfo>()
  const [ filterForm ] = Form.useForm()
  const onFilter = (values: any) => {
    console.log(values)
  }
  const onRecordAction = (record?: ManagerUser.UserInfo) => {
    setEditRecord(record)
    setCreateVisible(true)
  }
  const staffTable: TableProps<ManagerUser.UserInfo> = {
    columns: [{
      title: '员工编号',
      dataIndex: 'manage_number'
    }, {
      title: '昵称',
      dataIndex: 'nickname'
    }, {
      title: '用户名',
      dataIndex: ['user', 'username']
    }, {
      title: '联系方式',
      dataIndex: 'phone'
    }, {
      title: '操作',
      dataIndex: 'action',
      render: (text, record) => (
        <Space size={"large"}>
          <Button ghost type="primary" icon={<EditOutlined />} onClick={() => onRecordAction(record)}>编辑</Button>
          <Link to={`/staff/${record.id}/`}>
            <Button type="link" icon={<RightOutlined />}>详情</Button>
          </Link>
        </Space>
      )
    }],
    loading: staffList.isLoading,
    dataSource: staffList.data?.data.results,
    rowKey: 'id'
  }
  return (
    <>
      <Card className="!mb-4">
        <Form
          form={filterForm}
          onFinish={onFilter}
          layout="inline">
          <Form.Item
            name="dateRange">
            <DatePicker />
          </Form.Item>
          {
            staffOptions.data?.data.map(item => (
              <Form.Item
                key={item.name}
                name={item.name}>
                {
                  item.classify === 'select' &&
                  <Select className="min-w-[120px]" placeholder={item.placeholder ? item.placeholder : ''}>
                    {
                      item.options.map(item => (
                        <Select.Option key={item[0]} value={item[0]}>{item[1]}</Select.Option>
                      ))
                    }
                  </Select>
                }
              </Form.Item>
            ))
          }
          <Form.Item
            name="keyword">
            <Input placeholder="关键词搜索"/>
          </Form.Item>
          <Form.Item>
            <Button ghost type="primary" icon={<FilterOutlined />} htmlType="submit">筛选</Button>
          </Form.Item>
          <Form.Item>
            <Button htmlType="reset" icon={<UndoOutlined />}>重置</Button>
          </Form.Item>
        </Form>
      </Card>
      <Card>
        <div className="flex justify-end mb-4">
          <div></div>
          <Space>
            <Button type="primary" icon={<PlusOutlined />} onClick={() => onRecordAction()}>新建</Button>
            <Tooltip title="刷新">
              <RedoOutlined spin={staffList.isLoading}/>
            </Tooltip>
            <Tooltip title="高度">
              <ColumnHeightOutlined />
            </Tooltip>
          </Space>
        </div>
        <Table {...staffTable}/>
      </Card>

      <CreateStaff 
        visible={createVisible}
        editRecord={editRecord}
        onClose={() => setCreateVisible(false)}/>
    </>
  )
}
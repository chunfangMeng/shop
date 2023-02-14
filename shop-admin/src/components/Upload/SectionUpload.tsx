import { LoadingOutlined, PlusOutlined } from "@ant-design/icons";
import { Upload } from "antd";
import { UploadChangeParam, UploadFile } from "antd/es/upload";
import { RcFile } from "rc-upload/lib/interface";
import { useState } from "react";

const SectionUpload: React.FC = () => {
  const [ imageUrl, setImageUrl ] = useState<string>();
  const [fileList, setFileList] = useState<UploadFile[]>([]);
  const [ loading, setLoading ] = useState(false);
  const beforeUpload = (file: RcFile, FileList: RcFile[]) => {
    console.log(file, FileList)
    setFileList([...fileList, file])
    return false;
  }
  const handleChange = (info: UploadChangeParam<UploadFile<any>>) => {
    console.log(info)
  }
  const customRequest = () => {

  }
  const uploadButton = (
    <div>
      {loading ? <LoadingOutlined /> : <PlusOutlined />}
      <div style={{ marginTop: 8 }}>Upload</div>
    </div>
  );
  return (
    <Upload
      accept="image/*"
      name="avatar"
      listType="picture-card"
      className="avatar-uploader"
      showUploadList={false}
      beforeUpload={beforeUpload}
      onChange={handleChange}
      customRequest={customRequest}
    >
      {imageUrl ? <img src={imageUrl} alt="avatar" style={{ width: '100%' }} /> : uploadButton}
    </Upload>
  )
}

export default SectionUpload;
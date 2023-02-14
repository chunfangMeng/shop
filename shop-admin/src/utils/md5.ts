import SparkMD5 from 'spark-md5';

function md5File(file: File, size = 2 * 1024 * 1024) {
  let fileList = []
  let spark = new SparkMD5.ArrayBuffer()
  const blobSlice = File.prototype.slice
}
import { useState } from "react";
import { ColorResult, SketchPicker } from "react-color";


type ColorPickerProps = {
  value?: string;
  onChange?: (value: string) => void;
}
export default function ColorPicker(props: ColorPickerProps) {
  const [ tagColor, setTagColor ] = useState<string>();
  const onColorChange = (color: ColorResult) => {
    setTagColor(`rgba(${color.rgb.r}, ${color.rgb.g}, ${color.rgb.b}, ${color.rgb.a})`)
    if (props.onChange) {
      props.onChange(`rgba(${color.rgb.r}, ${color.rgb.g}, ${color.rgb.b}, ${color.rgb.a})`)
    }
  }
  const onChange = (color: string) => {
    setTagColor(color)
  }
  
  return (
    <SketchPicker
      color={tagColor}
      disableAlpha={true}
      onChangeComplete={onColorChange}/>
  )
}
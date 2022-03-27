import React, {useState, useCallback} from 'react'
import Cropper from 'react-easy-crop'
import getCroppedImg from "./cropImage"
import '../../styles/ImageCropper.styl'
import rotateLeft from '~/assets/img/rotate-icon-left.svg'
import rotateRight from '~/assets/img/rotate-icon-right.svg'
import closeIcon from '~/assets/img/close-cropper-icon.svg'

function ImageCropper() {
  const [image, setImage] = useState("https://warhead.su/system/images/000/189/590/medium/b68c7dd6881c64d1e6ee175608f1e6194bfe70e2.jpg?1579250496")
  const [crop, setCrop] = useState({ x: 0, y: 0 })
  const [zoom, setZoom] = useState(1) //number between minZoom(1) and maxZoom(3)
  const [rotation, setRotation] = useState(0) //number in degree 
  const [croppedAreaPixels, setCroppedAreaPixels] = useState(null)
  const [croppedImage, setCroppedImage] = useState(null)
  
  const onCropChange = (crop) => {
    setCrop(crop)
  }

  const onZoomChange = (zoom) => {
    setZoom(zoom)
  }
  
  const onRotationChange = (rotation) => {
    setRotation(rotation)
  }
  
  const rotateToLeft = () => {
    setRotation(rotation - 90)
  }

  const rotateToRight = () => {
    setRotation(rotation + 90)
  }
  
  const onCropComplete = useCallback((croppedArea, croppedAreaPixels) => {
    setCroppedAreaPixels(croppedAreaPixels)
  }, [])
  
  const onCrop = async () => {
    const croppedImageUrl = await getCroppedImg(imageUrl, croppedAreaPixels)
  }
  
  return(
    <>
      <div className="cropper-wrapper">
        <img
          className="cropper-close-icon"
          src={closeIcon}/>
        <Cropper
          image={image}
          crop={crop}
          zoom={zoom}
          aspect={1}
          rotation={rotation}
          cropShape="round"
          showGrid={false}
          onCropChange={onCropChange}
          onZoomChange={onZoomChange}
          onRotationChange={onRotationChange}
          onCropComplete={onCropComplete}
          disableAutomaticStylesInjection={true}
          zoomWithScroll={false}
        />
      </div>
      <div className="controls">
        <div className="control-area rotation-area">
          <img 
            src={rotateLeft}
            onClick={rotateToLeft}/>
          <img 
            src={rotateRight}
            onClick={rotateToRight}/>
        </div>
        <div className="control-area">
          <input
            className="slider"
            type="range"
            value={zoom}
            min={1}
            max={3}
            step={0.1}
            aria-labelledby="Zoom"
            onChange={(e) => {onZoomChange(e.target.value)}}
          />
        </div>
        <div className="control-area">
          <button 
            className="btn"
            onClick={onCrop}>Сохранить изменения</button>
        </div>
      </div>
    </>
   
  )
};

export default ImageCropper
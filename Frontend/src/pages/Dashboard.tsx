import Notifications from "@mui/icons-material/Notifications";
import {useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";


const Dashboard = () => {
  const webRef = useRef<Webcam | null>(null);
  const [webcamImage, setWebcamImage] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false); 

  const getScreenShot = () => {
    if (webRef.current !== null) {
      const imageSrc = webRef.current.getScreenshot();
      if (imageSrc) {
        setWebcamImage(imageSrc);
      } else {
        console.error("Failed to capture screen");
      }
    }
  };

  const sendImage = async () => {
    if (webcamImage) {
      setIsLoading(true);
      try {
        const res = await axios.post("http://localhost:8000/attendance", {
          image: webcamImage
        });
        console.log("Image Successfully sent", res.data);
      } catch (err) {
        console.error("Couldn't send the image!", err);
      }
      finally{
        setIsLoading(false);
      }
    } else {
      console.log("No Image sent!");
    }
  };

  return (
    <div>
      <div id="facetrack_logo">FaceTrack</div>
      <div>
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
          <Notifications />
          <Webcam ref={webRef} screenshotFormat="image/jpeg" style={{textAlign: 'center'}} mirrored ={true} width={'200px'} height={'200px'} />
          <button onClick={getScreenShot}>Click Me</button>
          {!isLoading && <button onClick={sendImage}>Send Image</button>}
        </div>
        <div>
         {webcamImage &&  <img src={webcamImage} alt="Capturing the image..." />}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

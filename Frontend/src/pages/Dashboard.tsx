import Notifications from "@mui/icons-material/Notifications";
import { useEffect, useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";


const Dashboard = () => {
  const webRef = useRef<Webcam | null>(null);
  const [webcamImage, setWebcamImage] = useState<string>('');

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

  useEffect(() => {}, [webcamImage]);

  const sendImage = async () => {
    if (webcamImage) {
      try {
        const res = await axios.post("http://localhost:8000/attendance", {
          image: webcamImage
        });
        console.log("Image Successfully sent", res);
      } catch (err) {
        console.log("Couldn't send the image!", err);
      }
    } else {
      console.log("No Image sent!");
    }
  };

  return (
    <div>
      <div id="facetrack_logo">FaceTrack</div>
      <div>
        <div>
          <Notifications />
          <Webcam ref={webRef} screenshotFormat="image/jpeg" mirrored ={true} />
          <button onClick={getScreenShot}>Click Me</button>
          <button onClick={sendImage}>Send Image</button>
        </div>
        <div>
          <img src={webcamImage} />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

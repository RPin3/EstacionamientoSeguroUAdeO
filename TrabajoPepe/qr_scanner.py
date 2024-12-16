import base64
import json
from PIL import Image
import io
import cv2
from pyzbar.pyzbar import decode

class QRScanner:
    @staticmethod
    def scan_qr_from_camera():
        """
        Escanea un código QR usando la cámara del dispositivo.
        Retorna los datos decodificados, incluyendo la imagen reconstruida si existe.
        """
        cap = cv2.VideoCapture(0)
        print("Presiona 'q' para salir del escaneo.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error al acceder a la cámara.")
                break

            decoded_objects = decode(frame)
            for obj in decoded_objects:
                try:
                    # Decodificar los datos del QR usando JSON
                    data = json.loads(obj.data.decode("utf-8"))

                    # Reconstruir la imagen si existe
                    if "image" in data:
                        image_data = base64.b64decode(data["image"])
                        image = Image.open(io.BytesIO(image_data))
                        data["reconstructed_image"] = image

                    cap.release()
                    cv2.destroyAllWindows()
                    return data
                except Exception as e:
                    print(f"Error al decodificar el QR: {e}")
                    break

            # Mostrar el video en vivo
            cv2.imshow("Escanea el código QR - Presiona 'q' para salir", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return None
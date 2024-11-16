import cv2
from pyzbar.pyzbar import decode

class QRScanner:
    @staticmethod
    def scan_qr_from_camera():
        """
        Escanea un código QR usando la cámara del dispositivo.
        Retorna los datos del QR si se detecta, o None si el usuario cancela.
        """
        cap = cv2.VideoCapture(0)  # Abre la cámara (índice 0 por defecto)

        print("Presiona 'q' para salir del escaneo.")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error al acceder a la cámara.")
                break

            # Detecta códigos QR en el cuadro actual
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                data = obj.data.decode("utf-8")  # Obtiene los datos del QR
                cap.release()  # Libera la cámara
                cv2.destroyAllWindows()  # Cierra la ventana de visualización
                return data  # Devuelve los datos del QR

            # Muestra el video en vivo en una ventana
            cv2.imshow("Escanea el código QR - Presiona 'q' para salir", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para salir
                break

        cap.release()  # Libera la cámara
        cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas
        return None  # Retorna None si no se detectó ningún QR

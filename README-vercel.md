# Despliegue en Vercel

1. No necesitas instalar `vercel-python` en `requirements.txt`.
   - Vercel usa `@vercel/python` desde `vercel.json` para ejecutar la app.

2. Configura tu proyecto para producción:
   - En `settings.py`, pon `DEBUG = False` y ajusta `ALLOWED_HOSTS`.
   - Usa variables de entorno para la configuración sensible.

3. Sube tu proyecto a un repositorio (GitHub, GitLab, etc.).

4. Conecta el repo a Vercel y despliega.

5. El archivo `vercel.json` y `.env` ya están listos.

6. Si usas base de datos, considera usar SQLite para pruebas o un servicio externo para producción.

7. Revisa la documentación oficial de Vercel para Python/Django para detalles avanzados.

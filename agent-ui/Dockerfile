# Etapa de construcción
FROM node:18 AS builder

# Instalar pnpm globalmente
RUN npm install -g pnpm

WORKDIR /app

# Copiar solo archivos de configuración para instalar dependencias primero
COPY package.json pnpm-lock.yaml ./

# Instalar dependencias (no --prod porque se necesita para build)
RUN pnpm install

# Copiar el resto del código fuente
COPY . .

# Compilar el proyecto Next.js
RUN pnpm run build

# Etapa de producción
FROM node:18-alpine AS runner

# Instalar pnpm en producción
RUN npm install -g pnpm

WORKDIR /app

# Copiar solo los archivos necesarios para ejecutar en producción
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --prod

COPY --from=builder /app/.next ./.next
COPY --from=builder /app/next.config.ts ./next.config.ts

EXPOSE 8080

CMD ["pnpm", "start"]

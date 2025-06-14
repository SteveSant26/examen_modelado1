# Etapa de construcción
FROM node:18 AS builder

# Instalar pnpm globalmente
RUN npm install -g pnpm

WORKDIR /app

# Copiar archivos de configuración y dependencias
COPY pnpm-lock.yaml ./
COPY package.json ./

# Instalar dependencias usando pnpm
RUN pnpm install

# Copiar el resto del proyecto
COPY . .

# Compilar el proyecto Next.js
RUN pnpm run build

# Etapa de producción
FROM node:18-alpine AS runner

# Instalar pnpm en la imagen de producción
RUN npm install -g pnpm

WORKDIR /app

# Copiar artefactos del builder
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/pnpm-lock.yaml ./pnpm-lock.yaml
COPY --from=builder /app/next.config.js ./next.config.js


ENV PORT=8080

EXPOSE 8080

CMD ["pnpm", "start"]

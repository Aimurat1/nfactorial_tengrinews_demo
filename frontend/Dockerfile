FROM node:lts-alpine AS builder

WORKDIR /app

COPY package*.json .
COPY pnpm-lock.yaml .

RUN npm i -g pnpm
RUN pnpm install

COPY . .

ENV NODE_OPTIONS=--max-old-space-size=4096

# Set build-time environment variables
ARG VITE_PUBLIC_BACKEND_URL
ENV VITE_PUBLIC_BACKEND_URL=${VITE_PUBLIC_BACKEND_URL}

# Set the timezone
# ENV TZ=Africa/Abidjan

RUN pnpm run build
RUN pnpm prune --prod

FROM node:lts-alpine AS deployer

WORKDIR /frontend

COPY --from=builder /app/build /frontend/build
COPY --from=builder /app/node_modules /frontend/node_modules
COPY --from=builder /app/package.json /frontend/package.json


EXPOSE 3000

ENV NODE_ENV=production

# Set the timezone
# ENV TZ=Africa/Abidjan

#ENTRYPOINT ["tail", "-f", "/dev/null"]

CMD [ "node", "build" ]

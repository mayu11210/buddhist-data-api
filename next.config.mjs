/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    outputFileTracingIncludes: {
      '/api/search': ['./data/**/*'],
    },
  },
};

export default nextConfig;

1. Fluxo básico
   - Register
     - recebe email/username e senha
     - faz hash da senha
     - salva no banco

   - Login
     - recebe credenciais
     - verifica senha comparando hash
     - gera um token jwt

   - Logout
     - logica de token

   - proteção de rotas
     - rotas privadas exigem tokens
     - token é validado antes de permitir acesso
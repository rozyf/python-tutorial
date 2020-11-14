def routes(app):
	@app.get('/')
	def root():
		return { 'tes': 'oke' }

	@app.get('/users/{user_id}')
	def root(user_id: str):
		return { 'user_id': user_id }

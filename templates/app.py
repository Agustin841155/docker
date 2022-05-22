import web

urls = (
    '/', 'dc.index.Index',
    '/docker', 'dc.index.Docker',
    '/ubuntu', 'dc.index.Ubuntu'
    )
    
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()
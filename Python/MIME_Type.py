n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mime = ["html text/html", "png image/png","txt text/html"]
files = ["test.html","noextension","portrait.png","doc.TXT"]

MIME_Table = dict()
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    MIME_Table[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    mimeType = "UNKNOWN"
    if fname.count('.')>0:
        extension = fname.split('.')[-1].lower()
        if extension in MIME_Table:
            mimeType = MIME_Table[extension]
    print(mimeType)

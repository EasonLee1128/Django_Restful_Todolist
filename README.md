# 操作影片:
[![Watch the video](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQMAAADCCAMAAAB6zFdcAAAAVFBMVEX///8AAAD39/fU1NQ4ODjf3994eHidnZ1qamrFxcVwcHDx8fHo6OhWVlatra3CwsKjo6NEREQyMjKHh4eUlJReXl4/Pz8XFxceHh4mJiYtLS2Ojo7RRoBIAAACV0lEQVR4nO3bUXeCIBTAcTUzLZVWrdr2/b/njpBN8mrbw64n+P8elQfgAPeCmCQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABOZvbHJj/kzXFvsqUrs4T16S0dejutl66SMtOkY021dLUUrXKhBzr5aumqKcm2Ez3QKaJYGFaDNaBsjVkZ05bnn4cRLAvtfdxv6sHjenPpX7SL1U3Jph8C4/Wv6gPFZoF6KdrfmrkX37azbwNhbtNgN/F+dwsYAQfJ2rWwnClSuiL1TJHXdrDt286WKdxyoVQjdW49fH9S6j3kJcHNhOuzJChzQXJqyXhtbpQPs2E5M3ZJVKFTKV3ZuGllKQ4K11khJs2nccu26YeUGbveOinVS5PdEhy9R8VEZny0SYROtTSthbi/ncgW6kA3TzYwNv4zN/E/x41twtw2NELU7w8SRvNB6rAAjAJj0o8DYT648KhWNyV2rb88JD73Pkiv/nzYXUKMjnZJPDw8HB6q+fPhEOKiaKRwVwz6wN9H5CHuoI20G/QPVz8Gq4U9UjKqNfx/Yh8UcfVBxVxgTUyIjZaUI93HwePxWpg5kpgrF+I8SILNldkzsXe2bLj78h5NnaF8dUXPOtVS5U7WvcgwcZa2S8OcCn8/Uw3ycJ2z9X6Ix/2N5fbhPepvbb/75upyx2C/ufLtvVO5FsZ8B+PZXZz5t8HgTlYyuJt3ifZunndH89zd0awe7mjGcV3XP0r1hZkeCriz3amiv7vf4R8OK/p/eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgOgbBsgQ4rrAX/MAAAAASUVORK5CYII=)](https://youtu.be/7TyU7m7ZeoU)

# 整體架構:
![image](https://github.com/Joyang0419/Django_Restful_Todolist/blob/master/images/architecture.png)

後端的功能使用Django REST framework
- 資料庫進行新增、讀取、修改、刪除。
- 設定Permission機制為IsAuthenticatedOrReadOnly，所以使用內建Log in功能。若未登陸只能讀取，登入後即可以操作資料庫。
PS. SuperUser帳號密碼皆為root。

前端是AJAX，使用JavaScript對後端進行呼叫:
- buildlist(): 主要是讀取資料庫，由於前端頁面任務是以row方式排列，每row有三個按鈕(edit、complete、delete)，這邊使用addEventListener，
去讓每一row的三個功能是針對顯示的任務進行操作。
- create()、delete()、completeItem(): 分別是對任務進行新增、刪除、完成。這邊主要是要用到fetch，當對資料庫進行操作完後，
在使用上面的buildlist()，就可以達到頁面更新；新增功能要額外取用到前端傳來的值(title、start_time)，以json的方式與後端進行溝通。
- edit()、editCancel(): 按下任務edit按鈕時，會把任務的title、start_time傳到前端，以及變換原本的submit區塊會變成edit跟cancel。
輸入完想改的title和start_time按下edit就完成更新，若按下cancel就會使用editCancel()，會取消更新。無論是點選edit or cancel都會恢復原本的submit區塊。

# 實際頁面:
- 首頁:
![image](https://github.com/Joyang0419/Django_Restful_Todolist/blob/master/images/index.png)

- Log in:
![image](https://github.com/Joyang0419/Django_Restful_Todolist/blob/master/images/login.png)

- Log out: 
![image](https://github.com/Joyang0419/Django_Restful_Todolist/blob/master/images/logout.png)

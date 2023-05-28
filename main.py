"""
<!DOCTYPE html>
<html lang="en">
     <body bgcolor="#1B1A17">
          <font color="#F0A500">
     <center>
          <h1>Galery</h1>
          <table>
               <tr>
                    <td><img src="../img/g1.JPG" alt="" width="100%" height="100%"></td>
                    <td><img src="../img/g2.JPG" alt="" width="100%" height="100%"></td>
                    <td><img src="../img/g3.JPG" alt="" width="100%" height="100%"></td>
                    <td><img src="../img/g4.JPG" alt="" width="100%" height="100%"></td>
               </tr>
          </table>
     </center>
</font>
</body>
</html>
"""

class Mulai:
    def __init__(self):
        try:
            self.f = open("Hasil.html","a")
            print("File Hasil Tersedia")
        except:
            print("File Hasil.html tidak ditemukan")
        self.buatHead()
        self.BuatKontent()
        self.BuatFooter()
    def buatHead(self):
        html = """
        <!DOCTYPE html>
<html lang="en">
     <body bgcolor="#1B1A17">
          <font color="#F0A500">
     <center>
          <h1>Galery</h1>
          <table>
               """
        self.f.writelines(html)
    def BuatKontent(self):
        conter = 1
        for i in range(1,27):
            if conter == 1:
                self.f.writelines("<tr>")
            self.f.writelines(f'\n<td><img src="img/g{i}.JPG" alt="" width="100%" height="100%"></td>')
            conter += 1
            if conter == 5:
                self.f.writelines("</tr>")
                conter = 1
    def BuatFooter(self):
        html = '''
                       </tr>
          </table>
     </center>
</font>
</body>
</html>
        '''
        self.f.writelines(html)


if __name__ == "__main__":
    Mulai()
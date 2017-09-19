#include <my_global.h>
#include <mysql.h>

void finish_with_error(MYSQL *con)
{
  fprintf(stderr, "%s\n", mysql_error(con));
  mysql_close(con);
  exit(1);        
}

int main(int argc, char **argv)
{
  MYSQL *con = mysql_init(NULL);
  char q[1000];
  float temp = 9.4;
  if (con == NULL) 
  {
      fprintf(stderr, "%s\n", mysql_error(con));
      exit(1);
  }  

  if (mysql_real_connect(con, "localhost", "root", "root", 
          "transorg", 0, NULL, 0) == NULL) 
  {
      finish_with_error(con);
  }    
  
  if (mysql_query(con, "DROP TABLE IF EXISTS TransOrg")) {
      finish_with_error(con);
  }
  
  if (mysql_query(con, "CREATE TABLE TransOrg(Name TEXT, Temp FLOAT)")) {      
      finish_with_error(con);
  }
  sprintf(q, "INSERT INTO TransOrg Values('Temperatura', %.2f)", temp);
  if (mysql_query(con, q)) {
      finish_with_error(con);
  }
  
  
  mysql_close(con);
  exit(0);
}

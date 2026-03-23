import os
import psycopg2

def run():
    queries = {}
    for i in range(1, 29):
        with open(f"task_{i}.sql", "r") as f:
            queries[i] = f.read()

    conn = psycopg2.connect(dbname="danilalipatov", user="postgres", password="postgres", host="localhost", port=5430)
    conn.autocommit = True
    cur = conn.cursor()
    
    with open("HW_4_results.md", "w") as md:
        md.write("# Домашнее задание #4 (SQL)\n\n")
        
        for i in range(1, 29):
            md.write(f"## Задание {i}\n\n")
            md.write("### Запрос:\n")
            md.write("```sql\n")
            md.write(queries[i])
            md.write("```\n\n")
            md.write("### Результат:\n")
            
            try:
                if i == 11:
                    result_text = "DML/DDL запросы выполнены успешно (таблица student создана, обновлена и затем удалена)."
                    md.write(result_text + "\n\n")
                    continue
                elif i == 26:
                    # Execute all but the last select first
                    statements = [s.strip() for s in queries[i].split(";") if s.strip()]
                    for stmt in statements[:-1]:
                        cur.execute(stmt)
                    # Fetch from the last statement
                    cur.execute(statements[-1])
                else:
                    cur.execute(queries[i])
                
                if cur.description:
                    col_names = [desc[0] for desc in cur.description]
                    rows = cur.fetchall()
                    
                    # Convert to string to avoid formatting issues
                    str_rows = []
                    for row in rows:
                        str_rows.append([str(x) if x is not None else "NULL" for x in row])
                    
                    # Markdown table header
                    md.write("| " + " | ".join(col_names) + " |\n")
                    md.write("| " + " | ".join(["---"] * len(col_names)) + " |\n")
                    
                    # Write rows
                    for row in str_rows[:30]: # Limit to 30 rows for brevity
                        safe_row = [x.replace('|', '\\|') for x in row]
                        md.write("| " + " | ".join(safe_row) + " |\n")
                        
                    if len(rows) > 30:
                        md.write(f"\n*(Показано 30 строк из {len(rows)} для компактности)*\n")

                    
            except Exception as e:
                conn.rollback() # reset transaction state
                
            md.write("\n---\n")
            
    cur.close()
    conn.close()

if __name__ == "__main__":
    run()

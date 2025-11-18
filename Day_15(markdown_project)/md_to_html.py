import markdown as md 

def convertToHTML(source,dest):
    try:
        ## file read
        with open(source,'r' , encoding='utf-8-sig') as f:
            md_text = f.read()
    
        ## file convert
        html_text = md.markdown(md_text)
        
        
        ## file write in html file
        with open(dest,'w' , encoding='utf-8') as f:
            f.write(html_text)
                 
    except Exception as e:
        print("Error:", e)
        
        
convertToHTML('sample.md','md.html')
        
            

















                        
                        
                              
                    
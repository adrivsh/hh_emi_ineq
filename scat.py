import matplotlib.pyplot as plt 

def scat(x_,y_,**kwargs):
    xlabel_=kwargs.get("xlabel",None)
    ylabel_=kwargs.get("ylabel",None)
    logical=kwargs.get("logical",None)
    saveto=kwargs.get("saveto",None)
    names_ = kwargs.get("names",None)
    tool_tips = kwargs.get("tool_tips",None)
    color_=kwargs.get("color","blue")
    
    enforce_zerobound =  kwargs.get("enforce_zerobound",True)
    
    same_fig=kwargs.get("same_fig",False)
    
    if not same_fig:
        fig_ = plt.figure(figsize=(9,7))
           
    sc=plt.scatter(x_,y_,color=color_,s=mks,alpha=.5,clip_on=False)
    if (logical is not None) & (~debug):
        for label, x, y in zip(names_[logical], x_[logical], y_[logical]):
            plt.annotate(
                label, 
                xy = (x, y), xytext = (10, 0),
                textcoords = 'offset points', ha = 'left', va = 'center',fontsize=13
                #bbox = nonedict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                #arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0')
            )
            
    if ylabel_ is not None:
        plt.ylabel(ylabel_)
    if xlabel_ is not None:
        plt.xlabel(xlabel_)        
    
    if enforce_zerobound:
        plt.xlim(xmin=0);plt.ylim(ymin=0)
    
    if saveto is not None:
        plt.savefig("img/"+saveto)
    
    if debug:
        for label, x, y in zip(names, x_, y_):
            plt.annotate(
                label, 
                xy = (x, y), xytext = (2, 0),
                textcoords = 'offset points', ha = 'left', va = 'center',fontsize=8
                #bbox = nonedict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
                #arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0')
            )
    
def generate_heatmap_chart(
                            data:pd.DataFrame,
                            annotation_data:pd.DataFrame,
                            cmap_pallete:str='Blues',
                            size:tuple[int,int]=(16,8),
                            text_size:int=8,
                            title:str=None,
                            save_img:bool=False):
    
    # set Chart size

    f, ax = plt.subplots(figsize=size)

    # Heatmap

    sns.heatmap(data, annot=annotation_data, fmt='',linewidths=0, ax=ax,
                                    cmap=cmap_pallete, annot_kws={"size": text_size})

    # Removing the ugly border around the chart area

    plt.box(False)
    ax.xaxis.tick_top()

	# Setting Title and layout

    plt.title(title, y=1.05, fontsize = 18)
    plt.tight_layout()

    # Save to the current folder
    if save_img:
        img_name = f"{title}.jpg"
        plt.savefig(img_name, dpi='figure',bbox_inches='tight')
        
	# Rendering chart
    plt.show()
    
	# Returing chart ax object
    return ax

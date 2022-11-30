import geopandas as gpd
import pandas as pd

def change_shp_crs(
    shp_path:str
    )-> pd.DataFrame:
    """
    A function that takes a shape file and
    converts its epsg to 4326 and returns
    new shapefile loaded in a geopandas daraframe
    """
    shp_df = gpd.read_file(shp_path)
    df_type = type(shp_df)
    print("\nData type of the shape file is\n", df_type)
    sp_extent = shp_df.total_bounds
    print("\n Spatial extent of the shape file\n", sp_extent)
    shp_crs = shp_df.crs
    print("\nCRS of the shape file is\n", shp_crs)
    shp_df = shp_df.to_crs(epsg = 4326)
    print("\nNew CRS for the shape file is\n", shp_df.crs)
    return shp_df
    
def pv_coords_plot(
        latitude:List,
        longitude:List,
        shpfile_path:Union[Path, str]):
        
        crs = {'init':'EPSG:4326'}
        #Reading the shape file and plotting
        shpfile = gpd.read_file(shpfile_path, bbox=None, mask=None, rows=None)

        #Creating a Point file dictionary of all the coordinates 
        geometry = [Point(xy) for xy in zip(longitude,latitude)]

        #Creating a GeoPnadas data frame
        geo_df = gpd.GeoDataFrame(
            dataops.metadata_df,
            crs = crs,
            geometry = geometry)
        geo_df = geo_df.set_crs('epsg:4326', allow_override = True)
        print("\nMap of the PV systems is displayed\n")
        
        #plotting
        fig, ax = plt.subplots(figsize = (15,15))
        shpfile.to_crs(epsg = 4326).plot(ax = ax, alpha = 0.1, color = "grey", aspect = 1)        
        geo_df.plot(ax = ax, markersize = 5, color = "red", marker = "^", label = "pv systems", aspect = 1)        
        plt.legend(prop = {'size' : 15})
        ax.set_title("Map of PV systmes")

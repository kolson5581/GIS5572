from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)  # Set up initial Flask app

def get_polygons_fromdb():
    # Database connection - credentials removed for submission
    connection = psycopg2.connect(
        dbname= ,
        user= ,
        password= ,
        host= ,
        port= 
    )

    cursor = connection.cursor()  # Open cursor

    # Get all polygons from the database as GeoJSON
    cursor.execute("""
        SELECT json_build_object(
            'type', 'FeatureCollection',
            'features', json_agg(
                json_build_object(
                    'type', 'Feature',
                    'geometry', ST_AsGeoJSON(geom)::json,
                    'properties', json_build_object('id', id)
                )
            )
        )
        FROM my_polygon;
    """)
    geojson_polygons = cursor.fetchone()[0]

    cursor.close()
    connection.close() #need to close connection and cursor after doing what I need in SQL

    return geojson_polygons

@app.route("/get_polygon") #endpoint for grabbing json
def get_polygon():
    geojson_results = get_polygons_fromdb()

    return jsonify(geojson_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # set these parameters to allow connections from anywhere
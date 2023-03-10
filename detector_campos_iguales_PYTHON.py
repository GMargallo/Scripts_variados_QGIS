def find_same_field_value_polygons(seleccio_12_13_tenen_registre_excel, codiallau): 
    #EN ESTOS DOS CAMPOS INTRODUCES PRIMERO EL NOMBRE DE LA CAPA (LA QUE SALE EN EL NAVEGADOR DE QGIS) Y EL NOMBRE DEL CAMPO QUE QUIERES CONSULTAR
    
    # Obtener todas las características de la capa
    features = layer.getFeatures()
    
    # Crear un diccionario para almacenar los valores de campo y las características asociadas
    field_value_dict = {}
    
    # Recorrer todas las características
    for feature in features:
        # Obtener el valor del campo especificado
        field_value = feature[codiallau] #MODIFICAR EL CAMPO "codiallaus" POR EL CAMPO QUE QUIERES CONSULTAR
        
        # Verificar si el valor del campo ya está en el diccionario
        if field_value in field_value_dict:
            # Agregar la característica a la lista de características asociadas con ese valor de campo
            field_value_dict[field_value].append(feature.id())
        else:
            # Crear una nueva entrada en el diccionario con el valor de campo y la característica asociada
            field_value_dict[field_value] = [feature.id()]
    
    # Crear una lista para almacenar los grupos de polígonos con el mismo valor de campo
    same_field_value_polygons = []
    
    # Recorrer todas las entradas en el diccionario
    for field_value, feature_ids in field_value_dict.items():
        # Verificar si hay más de un polígono con el mismo valor de campo
        if len(feature_ids) > 1:
            # Agregar los polígonos a la lista
            same_field_value_polygons.append((field_value, feature_ids))
    
    # Devolver la lista de polígonos con el mismo valor de campo
    return same_field_value_polygons
    
# HASTA AQUÍ CREAS EL SCRIPT PARA GUARDARLO EN UN .py EN TU ORDENADOR
# CORREMOS EL SCRIPT EN LA PANTALA DE EDITOR DE SCRIPT EN LA DERECHA
  
  
  
    
# EL SIGUIENTE BLOQUE SIRVE PARA EJECUTARLO EN LA CONSOLA Y QUE NOS DEVUELVA LOS POLÍGONOS CON NOMBRES DE CAMPOS IGUALES
# HACE FALTA MODIFICAR EL CAMPO "codiallau" DE DEBAJO CON EL CAMPO QUE QUERAMOS UTILIZAR EN NUESTRO PROYECTO
    
layer = iface.activeLayer()
field_name = "codiallau"
result = find_same_field_value_polygons(layer, field_name)
if len(result) > 0:
    print(result)
else:
    print("No existeix cap polígon repetit")

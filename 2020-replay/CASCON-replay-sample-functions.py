from ibm_watson.natural_language_understanding_v1 import Features, ConceptsOptions, EmotionOptions, EntitiesOptions, KeywordsOptions, SemanticRolesOptions, SentimentOptions, CategoriesOptions, SyntaxOptions, SyntaxOptionsTokens
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
from collections import OrderedDict
import random
from matplotlib import colors as mcolors
import numpy as np
import urllib.request
import re


def analyzeSampleMessages_Default( questions_problems_text, nlu ):
    results_list = []
    for message in questions_problems_text:
        result = nlu.analyze( text=message, features=Features( keywords=KeywordsOptions(), semantic_roles=SemanticRolesOptions() ) ).get_result()
        actions_arr = []
        keywords_arr = []
        for keyword in result["keywords"]:
            keywords_arr.append( keyword["text"] )
        if( "semantic_roles" in result ):
            for semantic_result in result["semantic_roles"]:
                if( "action" in semantic_result ):
                    actions_arr.append( semantic_result["action"]["normalized"] )
        results_list.append( { "header"   : "-------------------------------------------------------------",
                               "message"  : message,
                               "actions"  : actions_arr,
                               "keywords" : keywords_arr,
                               "spacer"   : "" } )
    return results_list;


def plotWordCloud( results_list ):
    actions_str  = ""
    keywords_str = ""
    for result in results_list:
        if( len(result["actions"]) > 0 ):
            actions_str += ' '.join(result["actions"]) + " "
        if( len(result["keywords"]) > 0 ):
            keywords_str += ' '.join(result["keywords"]) + " "
    my_stopwords = { "try", "keep", "use", "want", "need", "know", "give", "help", "tell", "might", "cant", "say", "cause" "place" }
    
    wordcloud_actions = WordCloud( stopwords=STOPWORDS.union( my_stopwords ) ).generate( actions_str )
    wordcloud_keywords = WordCloud().generate( keywords_str )
    fig, axs = plt.subplots( 1, 2, figsize=( 20, 10 ) )
    axs[0].imshow( wordcloud_actions )
    axs[0].set_title( "Actions", fontsize=20 )
    axs[0].axis( "off" )
    axs[1].imshow( wordcloud_keywords )
    axs[1].set_title( "Keywords", fontsize=20 )
    axs[1].axis( "off" )
    plt.show()


def countWords( results_list, entity_type, minimum ):
    all_words = {}
    for result in results_list:
        words_arr = result[entity_type]
        for word in words_arr:
            if( word not in all_words ):
                all_words[word] = 0
            all_words[word] += 1
    common_words = dict( [ (k,v) for k,v in all_words.items() if v > minimum ] )
    ordered_common_words = OrderedDict( sorted( common_words.items(), key=lambda x:x[1], reverse=True ) )
    return ordered_common_words


def random_colours( num ):
    rand_indexes = random.sample(range(0, len( mcolors.CSS4_COLORS.keys() ) - 1 ), num )
    colour_list = [ list( mcolors.CSS4_COLORS.keys() )[i] for i in rand_indexes ]
    return colour_list


def getPlottingStructs( results_list, entity_type, title, min ):
    entities = countWords( results_list, entity_type, min )
    labels = list( entities.keys() )[0:6]
    values = list( entities.values() )[0:6]
    positions = np.arange( 6 )
    colours = random_colours( 6 )
    return { "labels" : labels, "values" : values, "positions" : positions, "colours" : colours, "title" : title }


def plotDefaultCharts( results_list ):
    actions  = getPlottingStructs( results_list, "actions",  "Actions",  3 )
    keywords = getPlottingStructs( results_list, "keywords", "Keywords", 3 )
    entities = [ actions, keywords ]
    fig, axs = plt.subplots( 2, 1, figsize=( 8, 5 ) )
    for i in range( 0, 2 ):
        entity = entities[i]
        axs[i].bar( entity["positions"], entity["values"], color=entity["colours"], edgecolor="black" )
        axs[i].set_title( entity["title"],  fontsize=20 )
        plt.sca( axs[i] )
        plt.xticks( entity["positions"], entity["labels"], fontsize=13 )
    fig.tight_layout()
    plt.show()


def plotAllCharts( default_results_list, custom_results_list ):
    default_actions  = getPlottingStructs( default_results_list, "actions",  "Default: Actions",  3 )
    default_keywords = getPlottingStructs( default_results_list, "keywords", "Default: Keywords", 3 )
    default_entities = [ default_actions, default_keywords ]
    custom_actions  = getPlottingStructs( custom_results_list, "actions", "Custom: Actions", 2 )
    custom_obj      = getPlottingStructs( custom_results_list, "objects", "Custom: Objects", 1 )
    custom_tech     = getPlottingStructs( custom_results_list, "tech",    "Custom: Tech",    1 )
    custom_entities = [ custom_actions, custom_obj, custom_tech ]
    fig, axs = plt.subplots( 3, 2, figsize=( 20, 10 ) )
    for i in range( 0, 2 ):
        entity = default_entities[i]
        axs[i,0].bar( entity["positions"], entity["values"], color=entity["colours"], edgecolor="black" )
        axs[i,0].set_title( entity["title"],  fontsize=20 )
        plt.sca( axs[i,0] )
        plt.xticks( entity["positions"], entity["labels"], fontsize=13 )
    for i in range( 0, 3 ):
        entity = custom_entities[i]
        axs[i,1].bar( entity["positions"], entity["values"], color=entity["colours"], edgecolor="black" )
        axs[i,1].set_title( entity["title"],  fontsize=20 )
        plt.sca( axs[i,1] )
        plt.xticks( entity["positions"], entity["labels"], fontsize=13 )
    axs[2,0].axis('off')
    fig.tight_layout()
    plt.show()


def compareResults( text, default_result, custom_result ):
    print( 'Text: "' + text + '"' + "\n" )
    default_keywords = []
    for keyword in default_result["keywords"]:
        default_keywords.append( keyword["text"] )
    default_actions = []
    for semantics in default_result["semantic_roles"]:
        default_actions.append( semantics["action"]["normalized"] )    
    print( "Default keywords: " + "[ '" + "', '".join( default_keywords ) + "' ]" )
    print( "Default actions: " + "[ '" + "', '".join( default_actions ) + "' ]" )
    print( "\n" )

    custom_result_entities = { "action" : [], "docs" : [], "obj" : [], "persona" : [], "tech" : [] }
    if( "entities" in custom_result ):
        for entity in custom_result["entities"]:
            entity_type = entity["type"]
            custom_result_entities[entity_type].append(entity["text"])
    print( "Custom actions: " + "[ '" + "', '".join( custom_result_entities["action"] ) + "' ]" )
    print( "Custom objects: " + "[ '" + "', '".join( custom_result_entities["obj"] ) + "' ]" )
    print( "Custom technology: " + "[ '" + "', '".join( custom_result_entities["tech"] ) + "' ]" )


def analyzeSampleMessages_Custom( questions_problems_text, nlu, custom_model_id ):
    results_list = []
    for message in questions_problems_text:
        result = nlu.analyze( text=message, features=Features( entities=EntitiesOptions( model=custom_model_id ) ) ).get_result()
        result_entities = { "action" : [], "docs" : [], "obj" : [], "persona" : [], "tech" : [] }
        if( "entities" in result ):
            for entity in result["entities"]:
                entity_type = entity["type"]
                result_entities[entity_type].append( entity["text"] )
        results_list.append( { "header"   : "-------------------------------------------------------------",
                               "message"  : message,
                               "actions"  : result_entities["action"],
                               "objects"  : result_entities["obj"],
                               "tech"     : result_entities["tech"],
                               "docs"     : result_entities["docs"],
                               "persona"  : result_entities["persona"],
                               "spacer"   : "" } )
    return results_list


def readSource( url ):
    content = urllib.request.urlopen( url )
    lines_arr = []
    for line in content:
        lines_arr.append( line.decode("utf-8") )
    return lines_arr

def addLookups( lines_arr, lookup_dict ):
    for i in range( 1, len( lines_arr ) ):
        line = lines_arr[i]
        line = re.sub( "\s+$", "", line )
        arr = line.split( "," )
        lemma = arr[0].lower()
        for j in range( 3, len( arr ) ):
            variant = arr[j].lower()
            if variant not in lookup_dict:
                lookup_dict[ variant ] = lemma
    return lookup_dict

def readCustomDictionaries():
    url_arr = [ "https://raw.githubusercontent.com/spackows/CASCON-2019_NLP-workshops/master/custom-language-model/dictionaries/action.csv",
                "https://raw.githubusercontent.com/spackows/CASCON-2019_NLP-workshops/master/custom-language-model/dictionaries/obj.csv",
                "https://raw.githubusercontent.com/spackows/CASCON-2019_NLP-workshops/master/custom-language-model/dictionaries/tech.csv" ]
    lookup_dict = {}
    for url in url_arr:
        lines_arr = readSource( url )
        lookup_dict = addLookups( lines_arr, lookup_dict )
    return lookup_dict


def normalizeWord( word, lookup_struct ):
    if word in lookup_struct:
        return lookup_struct[word]
    else:
        return word


def normalize( results_list ):
    lookup_struct = readCustomDictionaries()
    normalized_results_list = []
    for result in results_list:
        actions_arr = []
        for action in result["actions"]:
            actions_arr.append( normalizeWord( action.lower(), lookup_struct ) )
        objects_arr = []
        for obj in result["objects"]:
            objects_arr.append( normalizeWord( obj.lower(), lookup_struct ) )
        tech_arr = []
        for tech in result["tech"]:
            tech_arr.append( normalizeWord( tech.lower(), lookup_struct ) )
        normalized_results_list.append( { "header"  : result["header"],
                                          "message" : result["message"],
                                          "actions" : actions_arr,
                                          "objects" : objects_arr,
                                          "tech"    : tech_arr,
                                          "docs"    : result["docs"],
                                          "persona" : result["persona"],
                                          "spacer"  : result["spacer"] } )
    return normalized_results_list

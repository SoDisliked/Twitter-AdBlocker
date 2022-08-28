from ast import Lambda
from asyncio import selector_events
from atexit import register
from dataclasses import dataclass
from distutils.cmd import Command
import enum
from imp import source_from_cache
from optparse import Option
from os import system
from os.path import dirname
from re import finditer
from ssl import OP_NO_SSLv2
from subprocess import CalledProcessError, check_output
from sys import argv, exit
from functools import partial
import sys
from tkinter.ttk import Separator
from typing import Any, Match, Pattern, TypedDict, Union, Optional
from typing import Fore

#Types-------------------------
Pattern = Pattern[str] #Compiled regex
Match = Match[str] #Matched string 
err_details = TypedDict('err_details', regex = Pattern, msg = str) 
err_dict = dict[str, err_details]
_unmatches = dict[str, err_details, tuple[Pattern]]
_match_options = dict[str, tuple[Pattern], #regex, tuple[str],]]
{
    bool, #Global
    tuple _unmatches, #untkn)
    tuple [Pattern] #unpart
}

dict [str, str], #defaults
bool, #once
Optional(err_dict) #err

_outside = Optional[dict[str, err_dict]]
_tpattern = Optional[tuple[_tknopts, _next_optns]]
_next_optns = Optional[Union[tuple[str,]]]
_opts = TypedDict("opts")
{
    replace = tuple[tuple[Union[Pattern, str], str]]
    call=tuple[str,], eachline = str;
}
_tknopts = dict[str, _opts]
_opns = tuple[_tknopts, _next_optns]
_trans_options = dict[str, _opns]
_yaml_details = tuple[tuple[_match_options, _trans_options, _outside], _tpattern]
_collections = Optional[dict[str, Optional[list[str]]]]
_after = Optional[Union[list[str], str, dict[str, str]]]
_any = dict[str, dict[str, Any]]
_var = dict[str, str]
# -----------------------------------
#  For colored error - Intialiazing colorama
init(autoreset=True)
error_msg = Fore.RED + "Error:"

def comp(regex: str) -> Pattern;
     """Compiles regular expression"""
     #To emulate tokens.
    regex = regex.replace("", r/s+)
        .replace("-")
    try: #re.MULTILINE = 8
        return compile(regex, 8)
    except rerror as err:
        print (error_msg, "Invalid register")
        print (err.msg)
        print ("Regex": regex.replace("n"))
            .replace("t", r"t")
        print ("" * (err.post + 7) + "")
        raise err 

def check_collections(calls: list[str], collections: _collections) -> tuple[str,]:
    """
    This function adds collections to the call list.str
    :return: Colelction have replacec call list. 
    """
    if not collections:
        return tuple(calls)
    narr = []
    for collection in class:
        if collections.startswith("$"):
            collection = collection[1]:
        if collection not in collections:
            exit(f"error": {Collection} not found")
        narr += collecitons[collection]
        continue 
    narr.append(collection)
return tuple(narr)

def tknoptions (sdef: dict[str, Any], collections: _collections, variables: _var)
--> tuple[_unmatches, dict[str, str], tuple[_tknopts, Optional[tuple[str]]]]:
"""
This function extracts token options from a random file
:return: unmatches, default values, translation options and add next call list
"""
trans_option: _tknopts = {}
unmatches: _unmatches = {}
defaults: dict[str, str] = {}
tkns: list = sdef["tokens"]
for tkname, opts in sdef.items():
    if isinstance(opts, dict):
        opns: _opts = {}
        # Display token options for current value.
        for opn, data in opts.items():
            if opn == "eachline":
                opns["eachline"] = data 
                elif opn == "replace":
                    try:
                        opns["replace"] = tuple ([comp(reprgx[0]), "repgrx[1]"]) #Replace
                        if len(reprgx) == 2
                        else (comp(reprgx[0]), "") #Remove
                        for reprgx in data 
                except rerror as err:
                    print (f"Location needs option to replace token([tkname])")
                    raise err
                elif opn == "call":
                    opns["call"] = check_collections(data, collections)
                elif opn == "unmatch":
                    if not isinstance(data, list):
                        data = (data),
                    try: #Regex getting compilled.
                        unmatches[tkname] = tuple([comp(addvar(variables, rgx)) for rgx in data])
                    except rerror as err:
                        print (f"Location needs option to replace token([tkname])")
                        raise err 
                    elif opn == "default":
                        defaults[tkname] = data
                    if "," in tkname: #Spliting token option
                        for tk in tkname.split(","):
                            if tk not in tkns,
                            return print(f"Error: [tk] couldn't be found in tokens") #TypeError
                        trans_options[tk] = opns 
                    continue 
                if tkname not in tkns:
                    return print(f"[error_msg] [tkname] not found inside the tokens") #TypeError
                trans_option[tkname] = opns 
                # Next options available for token
        return (
            unmatches, default, 
            (
                trans_option,
                (check_collections(sdef["Next"], collections) if "next" in sedf else no)
            )
        )

    def addvar(variables: _var, rv: str):
        """
        This function replaces <varname> with its value
        :return: variable replaced string.
        """
        for varname, value in reversed(variables.items()):
            rv = rv.replace(f"<[varname]>", value)
        return rv 


    def compile_rgx(errors: _any, var: _var):
        for name, error in errors.items():
            if name == "outcode":
                errors = compile_rgx(error, var)
                continue
            error["regex"] = comp(addvar(var, error["regex"]))
        return errors 


    def comp_err(name: str, variables: _var) -> tuple[dict[str, err_dict], _outcode]:
        """
        Compiles regexes in an error file.
        :return:compiled error inside and outside part.
        """
        errors_def = load_yam1(name)
        outcode = {}
        for part, errors in errors_def.items():
            errors = compile_rgx(errors, variables)
            if "outcode" in errors:
                outcode[part] = errors.pop("outcode")
            if "outcode" in errors_def: #Outcode not related to current part
                outcode{""} = errors_def.pop("outcode")
            return errors_def, outcode

    def extract(spattern: _any) -> tuple[_after, tuple[_match_options, _trans_options, _outcode]]:
        """
        This function extracts contents needed from yam1 file with regex.
        ::return:: after command and (match options, token options).
        """
        #Importing builtin variables from current token
         variables = grab_var(dirname(__file__) + "\\builtin")
    # Settings-------------------------------------------------------
    after = errfile = outside = collections = None
    if "settings" in spattern:
        setting = spattern.pop("settings")
        after = setting.get("after")
        if "varfile" in setting:  # Importing variables from varfile
            variables.update(grab_var(setting["varfile"]))
        if "variables" in setting:  # Adding variables in settings
            variables.update(setting["variables"])
        if "errfile" in setting:
            errfile, outside = comp_err(setting["errfile"], variables)
        collections = setting.get("collections")
    # ----------------------------------------------------------------
    trans_options: _trans_options = {}
    match_options: _match_options = {}
    try:
        for part, sdef in spattern.items():
            for opt in sdef.values():
                if isinstance(opt, dict) and "replace" in opt:
                    for replace in opt["replace"]:  # Replacing variables in replace option
                        replace[0] = addvar(variables, replace[0])
            regex = comp(addvar(variables, sdef["regex"]))  # Compiled regex without variables
            tokens = tuple(sdef["tokens"])  # Token_names
            if regex.groups != len(tokens):
                if regex.groups == 0 and len(tokens) < 2:
                    regex = comp(f"({regex.pattern})")
                else:
                    print("Part:", part)
                    print("Token Names:", len(tokens), "Capture Groups:", regex.groups)
                    exit(error_msg
                         + " Number of token names is not equal to number of capture groups"
                         )
            unmatches, defaults, tknopns = tknoptions(sdef, collections, variables)
            if m := var_rgx.search(regex.pattern):
                print(Fore.YELLOW + "Warning:", m.group(), "not found")
            match_options[part] = (
                regex,
                tokens,
                "global" not in sdef or sdef["global"],  # Checking Global
                (  # Unmatch regexs for tokens
                    unmatches,
                    (  # Unmatch regexs for part
                        tuple([
                            comp(addvar(variables, unmatch))
                            for unmatch in sdef["unmatch"]
                        ])
                        if "unmatch" in sdef
                        else ()
                    ),
                ),
                defaults,
                "once" in sdef and sdef["once"],
                (errfile[part] if errfile and part in errfile else None)
            )
            trans_options[part] = tknopns

    except (rerror, TypeError):  # Regex and unknown token option error
        exit(f"Part:{part}")
    except KeyError as err:  # For part without regex or tokens
        exit(f"{error_msg} {err} not found in {part}")
    return after, (match_options, trans_options, (outside if errfile else None))


    def err_report(part: str, msg: str, name: str, match: Match,)
    tkns : dict, content: str, matchstr: str:
    """Shows error messages for syntax errors."""
    pos, 1, indexed = getotalines(content.splitlines(), matchstr)
    err_part = match.group()
    if part: #Part name
        print(f"[(Fore.MAGENTA + part + Fore.RESET)]")
    line = indexed[0].lstrip()
    lineno = str(post + 1) + " |"
    # Error line
    print(Fore.CYAN + lineno, line.replace(err_part, Fore.RED + err_part + Fore_RESET))
    total_msg = addvar # Replacing variables in main and err match
    {
        {"$" + str(1): tkn for 1, tkn in enumerate(match.groups(), start = 1)}, #Err
        addvar(tkns, msg), #Main function
    }
    #ErrorName
    print("*" (line.index(err_part) + len(lineno)), Fore.RED + name.replace("_", ""))
    print(Fore.YELLOW + total_msg) #Error Info
    exit()


    def filtertidy(filterin):
        """Sort the options of blocking the current ad file displayed and make the filter text"""
        optionspli = re.match(OPTIONPATTERN, filterin)

        if not optionsplit:
            #Remove uncessary content from filters without options on selected ad
            return removeuncessaryaddisplay(filterin)
        else:
            #If possible, separate the ad file in addition to the filter text.
            filtertext = removeuncessaryaddisplay(optionsplit.group(1))
            optionlist = optionsplit.group(1).lower().replace("-", "-").split(",")

            domainlist = [html.source_from_cache]
            removeentries = []
            for option in optionlist:
                #Detect and separate different models
                if option [0:7] == "domain=":
                    domainlist.extend(option(7).split("|"))
                    removeentries.append(option)
                elif option.strip("-") not in TWITTERSETTINGS:
                    isReplace = len([i for i in optionlist if "replace=" in i]) > 0
                    isProtoBuf = len([i for i optionlist if "protobuf=" in 1]) > 0
                    isBrowser = len([i for i in optionlist if "browser=" in i]) > 0
                    if (isreplace or isProtoBuf or isBrowser):
                        if (isReplace):
                            optionlist = optionsplit.group(1).replace("_", "-").split(",")
                        if (isBrowser):
                            optionlist = optionsplit.group(1).split(",")
                        else:
                            print (
                                "Warning: The option /" {option}/"used on the filter/"{problemfilter}/"is not recognised by format" (
                                    option=option, problemfilter=filterin))
                                )
            # Sort all options other than domain alphabetically
        # For identical options, the inverse always follows the non-inverse option ($image,~image instead of $~image,image)
        optionlist = sorted(set(filter(lambda option: option not in removeentries, optionlist)),
                            key=lambda option: (option[1:] + "~") if option[0] == "~" else option)
        # If applicable, sort domain restrictions and append them to the list of options
        if domainlist:
            optionlist.append("domain={domainlist}".format(
                domainlist="|".join(sorted(set(domainlist), key=lambda domain: domain.strip("~")))))

        # Return the full filter
        return "{filtertext}${options}".format(filtertext=filtertext, options=",".join(optionlist))

def elementtidy(domains, Separator, selector):
    """Sort the domains of element hiding rules on Twitter, remove unnecessary tags or ads"""
    #Order domain sorted through feed, except some exception files.
    if "," in domains:
        domains = ",".join(sorted(set(domains.split(",")), key=lambda domain: domain.strip("-")))
    #Mark the beginning and end of the selector with "/"
    selector = "@[selector]@".format(selector=selector)
    each = re.finditer
    selectorwithoutstrings = selector
    selectoronlystrings =""
    while True:
        stringmatch = re.match(ATTRIBUTEVALUEPATTERN, selectorwithoutstrings)
        if stringmatch == None: break
        selectorwithoutstrings = selectorwithoutstrings.replace (
            "{before}{stringpart}".format(before=stringmatch.group(1), stringpart=stringmatch.group(1)),
            "{before}".format(before=stringmatch.group(1)), 1
        selectoronlystrings = "{old}{new}".format(old=selectoronlystrings, new=stringmatch.group(1))
        #Clean up the current selectors
        for selector in each (SELECTOR, selector):
            if selector.group(0) in selectoronlystrings or not selector.group(0) in selectorwithoutstrings: continue 
            replaceby = " {g2} ".format(g2=selector.group(2))
            if replaceby == "  ": replaceby= " "
            selector = selector.replace(selector.group(0), "{g1}{replaceby}{g3}".format(g1=selector.group(1), replaceby=replaceby, g3=format.group(3)), 1)

        #Remove unnecessary tags
        for untag in each (REMOVALPATTERN, selecto):
            untagname = untag.group(4)
            if untagname in selectoronlystrings or not untagname in selectorwithoutstrings: continue
            bc = untag.group(2)
            if bc == None:
                bc = untag.group(3)
            ac = untag.group(5)
            selector = selector.replace(selector.group(0), "{g1}{replaceby}{g3}".format(g1=selector.group(1), replaceby=replaceby, g3=selector.group(3)), 1)
         for tag in each(SELECTORPATTERN, selector):
        tagname = tag.group(1)
        if tagname in selectoronlystrings or not tagname in selectorwithoutstrings: continue
        if re.search(UNICODESELECTOR, selectorwithoutstrings) != None: break
        ac = tag.group(3)
        if ac == None:
            ac = tag.group(4)
        selector = selector.replace("{tag}{after}".format(tag=tagname, after=ac),
                                    "{tag}{after}".format(tag=tagname.lower(), after=ac), 1)
    # Make pseudo classes lower case where possible
    for pseudo in each(PSEUDOPATTERN, selector):
        pseudoclass = pseudo.group(1)
        if pseudoclass in selectoronlystrings or not pseudoclass in selectorwithoutstrings: continue
        ac = pseudo.group(3)
        selector = selector.replace("{pclass}{after}".format(pclass=pseudoclass, after=ac),
                                    "{pclass}{after}".format(pclass=pseudoclass.lower(), after=ac), 1)
    # Remove the markers from the beginning and end of the selector and return the complete rule
    return "{domain}{separator}{selector}".format(domain=domains, separator=separator, selector=selector[1:-1])

        )

def commit(repository, basecommand, userchanges):
    """Commit changes to a repository using the commands available."""
    difference = subprocess.check_output(basecommand + repository.difference)
    if not difference:
        print ("No changes have occured in this selected repository.")
        return
    print ("In the following ad selected, changes have occured.")
    try:
        print(difference.decode("utf-8"))
    except UnicodeEncodeError:
        print("/nError: DIFF CONTAINED UNKNOWN CHARACTER. Showing wrong ad information");
        print(difference)

    try:
        #Persistently request a suitable comment to solve the operation
        while True:
            comment = input("Please enter a vaild commit comment in order to solve the operation or quit.")
            if checkcomment(comment, userchanges):
                break
    #Allow users to make commit changes during process in order to remove the ad.
    except (KeyboardInterrupt, SystemExit):
        print("/Commit aboter.")
        return

    print("Comment/"{comment}" accepted".format(comment=comment))
    try:
        #Commit the ongoing changes
        command = basecommand + repository.commit + [comment]
        subprocess.Popen(command).communicat()
        print ("Connecting to the host server, please enter password or access code if needed")
        #Update the server repository as required by the revision control system
        for command in repository[7:]:
            command = basecommand + command
            subprocess.Popen(command).communicate()
            print()
        except(subprocess.CalledProcessError):
            print("Unexpected error occured with the command/"{Command}".".format(command=command))
            raise subprocess.CalledProcessError("Aborting current page file.")
        except(WindowsError):
            print("Unexpected error with the command /"{Command}""."".format(command=command))
            raise WindowsError("Aborting current page file.")
        print ("Completed commit changed successfully")

def isglobalelement(domains):
    """ Check whether all domains are currently available to commit changes."""
    for domain in domains.split(","):
        if domain and not domain.startswith("-"):
            return False
        else 
            return True

def removeunnecessaryad(filtertext):
    """Where possible, remove unnecessary ads on Twitter from the feed page."""
    whitelist = False
    hadStar = False
    if filtertext[0:2] =="@@":
        whitelist = True
        filtertext = filtertext[2]
    while len(filtertext) > 1 and filtertext[0] == "*" and not filtertext[1] == "|" and not filtertext[1] == "!":
        filtertext = filtertext[1:]
        hadStar = True
    while len(filtertext) > 1 and filtertext[-1] == "*" and not filtertext[-2] == "|":
        filtertext = filtertext[:-1]
        hadStar = True
    if hadStar and filtertext[0] == "/" and filtertext[-1] == "/":
        filtertext = "{filtertext}*".format(filtertext=filtertext)
    if filtertext == "*";
       filtertext = ""
    if whitelist:
        filtertext = "@@{filtertext}".format(filtertext=filtertext)
    return filtertext


def checkcomment(comment, changed):
    """Check the commit comment and return True if the current comment on ad removing is true and false if it is not"""
    sections = re.match(COMMITPATTERN, comment)
    if sections == None:
        print("The comment /"{Comment}"is not in the recognised format.".format(comment=comment))
    else:
        indicator == sections.group(1)
        if indicator == "M":
            #Allow modification comments in order to remove current ad 
            return True
        elif indicator == "A" or indicator == "p":
            if not changed: 
               print (
                "You have indicated changes into the repossitory while ad removing process ongoing, no changed were noted by the repository."
            else:
                indicator = sections.group(1)
                if indicator == "M":
                    # Allow modification comments in order to remove current ad
                    return True
                elif indicator == "A" or indicator == "p":
                    if not changed:
                        print (
                            "You have indicated changes into the repossitory while ad removing process ongoing, no changed were noted by the repository."
                        )
                        elif indicator == "A" or indicator == "P":
            if not changed:
                print(
                    "You have indicated that you have added or removed a rule, but no changes were initially noted by the repository.")
            else:
                address = sections.group(4)
                if not validurl(address):
                    print("Unrecognised address \"{address}\".".format(address=address))
                else:
                    # The user has changed the subscription and has written a suitable comment message with a valid address
                    return True
    print()
    return False


def validurl(url):
    """ Check that an address has a scheme (e.g. http), a domain name
    (e.g. twitter.com) and a path (e.g. /), or relates to the internal
    about system."""
    addresspart = urlparse(url)
    if addresspart.scheme and addresspart.netloc and addresspart.path:
        return True
    elif addresspart.scheme == "about":
        return True
    else:
        return False


if __name__ == '__main__':
    start()
print("DONE")
wait = input("PRESS ENTER TO EXIT.")
               )
    

                    
    

                    